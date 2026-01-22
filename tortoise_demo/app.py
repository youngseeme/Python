from datetime import datetime, timedelta
from tortoise import Tortoise, run_async
from config import TORTOISE_ORM
from models import Appointment, Doctor, Patient
import asyncio

async def main():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas() # 첫 실행 때만!

    # Create(insert)
    dr_lee = await Doctor.create(name="이병헌", specialty="내과")
    dr_park = await Doctor.create(name="박명수", specialty="소아과")

    p_lee = await Patient.create(name="이동원", birth_date="1993-01-01", phone='010-1234-1234')
    p_kim = await Patient.create(name="김민찬", birth_date="2000-05-10", phone='010-2345-3456')

    d_lee = await Doctor.get(name='박명수')
    p_lee = await Patient.get(name='김민찬')

    appt1 = await Appointment.create(
        patient=p_lee, doctor=d_lee,
        visit_date=datetime.now() + timedelta(days=1),
        note="초진 예약"
    )
    appt2 = await Appointment.create(
        patient=p_lee, doctor=dr_park,
        visit_date=datetime.now() + timedelta(days=2),
        note="소아과 상담"
    )

    # Read(select * from )
    appointments = await Appointment.all().select_related('patient', 'doctor')
    for appointment in appointments:
        print(appointment.id, appointment.visit_date, appointment.doctor, appointment.patient)

    app = await Appointment.filter(name='이동원')[0]
    print(app.id)
    app2 = await Appointment.get(name='이동원')
    
    # Update
    app2.visit_date = '2025-10-28'
    await app2.save()

    # Delete
    await app2.delete()


if __name__ == "__main__":
    asyncio.run(main())
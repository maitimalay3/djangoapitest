import datetime
import json
import pandas as pd
import wind_test.revenue.revenue as rev
import wind_test.operationcost.costcalc as opex
from api.models import LongRunningTask
from celery import shared_task


@shared_task
def process_wind_test_calculation(
        task_id,
        revinputdata,
        contractinfo,
        costinput
    ):
    print('def process_wind_test_calculation')
    print(task_id)
    RevObject = rev.turnover(revinputdata, contractinfo)
    Revdf = RevObject.RevenueCal()
    print(Revdf)

    CostObject = opex.opexcost(costinput, contractinfo)
    Costdf = CostObject.OpexCal()
    print(Costdf)

    # --------------------------Tax Input--------------------------------
    unlcashflow = pd.merge(Revdf, Costdf, left_on="dates", right_on="dates")
    print(unlcashflow)
    task = LongRunningTask.objects.get(id=task_id)
    task.state = LongRunningTask.COMPLETE_STATE
    cost = {row['dates']: row for row in json.loads(Revdf.to_json(orient="records"))}
    revenue = {row['dates']: row for row in json.loads(Revdf.to_json(orient="records"))}
    tax = {row['dates']: row for row in json.loads(unlcashflow.to_json(orient="records"))}
    task.result = {
        "cost": cost,
        "revenue": revenue,
        "tax": tax
    }
    task.save()
    return task.result
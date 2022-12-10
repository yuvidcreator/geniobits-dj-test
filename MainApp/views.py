import csv
import json
import datetime

from django.shortcuts import render

from .forms import UploadedCSVFileForm
from .models import UploadedCSVFile, Candle
# Create your views here.







def upload_csvfiles_view(request):
    form = UploadedCSVFileForm(request.POST or None, request.FILES or None)
    newjson = r'dummy.json'
    i = 0
    json_data = []
    if form.is_valid():
        form.save()
        form = UploadedCSVFileForm()
        obj = UploadedCSVFile.objects.get(active=False)
        with open(obj.file_name.path, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                # print(row)

                i += 1

                data = {
                    "id": i,
                    "name": row[0],
                    "date": datetime.datetime.strptime(row[1],'%Y%m%d').date().isoformat(),
                    "time": datetime.datetime.strptime(row[2], '%H:%M').time().isoformat(),
                    "open": row[3],
                    "high": row[4],
                    "low": row[5],
                    "close": row[6],
                    "volume": row[7]
                }

                # print(data)
                Candle.objects.create(
                    name = row[0],
                    date = datetime.datetime.strptime(row[1],'%Y%m%d').date().isoformat(),
                    time = datetime.datetime.strptime(row[2], '%H:%M').time(),
                    open = float(row[3]),
                    high = float(row[4]),
                    low = float(row[5]),
                    close = float(row[6]),
                    volume = int(row[7]),
                )
                json_data.append(data)

            obj.active = True
            obj.save()

        with open(newjson, 'w', encoding='utf-8') as jsonf:
            download_file = jsonf.write(json.dumps(json_data, indent=4))
            # UploadedCSVFile.objects.update(
            #     jsonfile=newjson
            # )
            # obj.jsonfile=newjson
            # obj.save()

    context = {
        "form": form,
        "download_file": newjson
    }
    return render(request, 'index.html', context)
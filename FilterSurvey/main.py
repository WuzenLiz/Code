"""customtool
    - read from file ./data.json
    - get data from file
    - data ['username','mobile','yearOfBirth','govId','gender']
    - write to file ./result.excel
    * json template
    {
        "paging": {
            "page": 1,
            "itemsPerPage": 200,
            "totalItems": 187
        },
        "result": [
            {
                "id": "ac140093-8507-18f1-8186-393ff4e37475",
                "metadata": {
                    "id": "ac140093-8507-18f1-8186-393ff4e37475",
                    "surveyId": "c3a0d93c-4781-412a-b59f-ed2073116102",
                    "tenantId": "ac140093-8507-18f1-8186-085a721151bb",
                    "username": "Nguyễn Thi Tuyết",
                    "yearOfBirth": 1970,
                    "mobile": "0989685983",
                    "govId": "034170005977",
                    "medicalCode": "",
                    "gender": "FEMALE",
                    "email": "",
                    "country": "Việt Nam",
                    "province": "Thái Bình",
                    "district": "Quỳnh Phụ",
                    "ward": "Quỳnh Hồng",
                    "address": "Luong Cụ Nam",
                    "point": 6.0,
                    "additionalData": "{\"points\":{\"gender\":0,\"age\":2,\"diabetes\":0,\"bmi\":0,\"waist\":2,\"bloodPressure\":2},\"sideEffects\":[]}",
                    "diseaseDiagnosis": [
                        "HYPERTENSION_HISTORY_MEDICATED",
                        "DIABETES_FILTER_POSITIVE"
                    ],
                    "diseaseResult": [
                        "HYPERTENSION_UNMEDICATED",
                        "DIABETES_POSITIVE"
                    ],
                    "tracking": [
                        "DIABETES_NONE"
                    ],
                    "educationLevel": "SECONDARY_SCHOOL",
                    "job": "FARMER",
                    "jobDetail": "Nông dân",
                    "averageIncome": "LESS_THAN_TWO",
                    "createdAt": "2023-02-10",
                    "createdBy": "hanh034179001358",
                    "updatedAt": "2023-06-09",
                    "updatedBy": "tytquynhhong"
                },
                "questions": null
            },
            ...
        ]
    }
"""
import json
import os
import sys

from xlwt import Workbook


# read from file
if __name__ == '__main__':
    try:
        with open('./data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('File not found')
        sys.exit(1)

    if os.path.exists('./result.xls'):
        os.remove('./result.xls')

    # get data from file
    data = data['result']

    # write to file
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Họ và Tên')
    sheet1.write(0, 1, 'Số điện thoại')
    sheet1.write(0, 2, 'Năm sinh')
    sheet1.write(0, 3, 'Số CMT& CCCD')
    sheet1.write(0, 4, 'Giới tính')

    for i in range(len(data)):
        sheet1.write(i + 1, 0, data[i]['metadata']['username'])
        sheet1.write(i + 1, 1, data[i]['metadata']['mobile'])
        sheet1.write(i + 1, 2, data[i]['metadata']['yearOfBirth'])
        sheet1.write(i + 1, 3, data[i]['metadata']['govId'])
        if data[i]['metadata']['gender'] == 'FEMALE':
            sheet1.write(i + 1, 4, 'Nữ')
        else:
            sheet1.write(i + 1, 4, 'Nam')
    wb.save('./result.xls')
    print('Done')


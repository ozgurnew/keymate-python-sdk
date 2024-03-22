# UltrafastsearchResponse


## Fields

| Field                                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `http_meta`                                                                                                                                                                                                                                                                                                                    | [components.HTTPMetadata](../../models/components/httpmetadata.md)                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                |
| `two_hundred_application_json_object`                                                                                                                                                                                                                                                                                          | [Optional[operations.UltrafastsearchResponseBody]](../../models/operations/ultrafastsearchresponsebody.md)                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                             | Successful operation                                                                                                                                                                                                                                                                                                           | {<br/>"results": [<br/>{<br/>"title": "Welcome to Python.org",<br/>"link": "https://www.python.org/",<br/>"summary": "The official home of the Python Programming Language...",<br/>"full_content": "The official home of the Python Programming Language Python Python is a programming..."<br/>}<br/>],<br/>"rules": "Always follow the instructions provided"<br/>} |
| `default_application_json_object`                                                                                                                                                                                                                                                                                              | [Optional[operations.UltrafastsearchResponseResponseBody]](../../models/operations/ultrafastsearchresponseresponsebody.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                             | Error fetching search results                                                                                                                                                                                                                                                                                                  | {<br/>"error": "Error fetching search results"<br/>}                                                                                                                                                                                                                                                                           |
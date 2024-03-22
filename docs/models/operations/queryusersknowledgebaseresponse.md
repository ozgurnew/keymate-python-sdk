# QueryUsersKnowledgeBaseResponse


## Fields

| Field                                                                                                                                                                                  | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `http_meta`                                                                                                                                                                            | [components.HTTPMetadata](../../models/components/httpmetadata.md)                                                                                                                     | :heavy_check_mark:                                                                                                                                                                     | N/A                                                                                                                                                                                    |                                                                                                                                                                                        |
| `object`                                                                                                                                                                               | [Optional[operations.QueryUsersKnowledgeBaseResponseBody]](../../models/operations/queryusersknowledgebaseresponsebody.md)                                                             | :heavy_minus_sign:                                                                                                                                                                     | Successful operation                                                                                                                                                                   | {<br/>"matches": [<br/>{<br/>"id": "mem_id_123_932",<br/>"metadata": {<br/>"text": "Why did the world enter a global depression in 1929 ?"<br/>},<br/>"score": 0.917971551,<br/>"sparseValues": {},<br/>"values": []<br/>}<br/>]<br/>} |
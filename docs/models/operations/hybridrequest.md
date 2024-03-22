# HybridRequest


## Fields

| Field                                                                                                                          | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `q`                                                                                                                            | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Search query                                                                                                                   |
| `percentile`                                                                                                                   | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Start it as '3', increase to '6' if ResponseTooLarge occurs, only reduce to '1' or '2' if user requests it.                    |
| `numofpages`                                                                                                                   | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Start it as '3'. Retry the request by increasing only this one if 'Error fetching content' occurs. Should be between 1 and 10. |
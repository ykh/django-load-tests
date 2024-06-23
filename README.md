## Django Load Tests Project

This project aims to provide an overview of Django's performance under different load scenarios.

### Machines Specifications

| Machine ID | CPU Vendor ID | CPU Model                                | CPU Cores | RAM | HDD |
|------------|---------------|------------------------------------------|-----------|-----|-----|
| M1         | GenuineIntel  | Intel(R) Core(TM) i5-10500 CPU @ 3.10GHz | 12        | 32  | SSD |

### API Methods Specifications

| Method ID | API Name    | HTTP Method | DB | ORM | ODM | DRF API | Serializer | Response           |
|-----------|-------------|-------------|----|-----|-----|---------|------------|--------------------|
| A1        | Return True | GET         | \- | \-  | \-  | APIView | \-         | `{"result": True}` |

### Reports

#### Columns Definitions

* **Users:** Concurrent users that sending requests to the API method.
* **RU:** Ramp-up users each second.
* **WT:** Random waiting time between each requests in second.
* **SGI:** WSGI or ASGI server name.
* **SGI W:** Number of SGI workers handling HTTP requests.
* **Duration:** Load test total time in minutes.
* **Requests:** Total requests within the test duration time.
* **Fails:** Failed requests number.
* **RPS:** Approx. of requests number per second.
* **AVG RT:** Average response time in millisecond.
* **Min RT:** Minimum response time in millisecond.
* **Max RT:** Maximum response time in millisecond.

#### Reports Table

| Report ID | Method ID | Machine ID | Users | RU  | WT          | SGI           | SGI W | Duration | Requests | Fails | RPS   | Avg RT | Min RT | Max RT |
|-----------|-----------|------------|-------|-----|-------------|---------------|-------|----------|----------|-------|-------|--------|--------|--------|
| R1        | A1        | M1         | 100   | 100 | 0.01 - 0.02 | Gunicorn      | 25    | 3m       | 159075   | 0     | 909   | 93.01  | 29     | 1160   |
| R2        | A1        | M1         | 100   | 100 | 0.01 - 0.02 | Django Server | \-    | 3m       | 34496    | 0     | 196.5 | 493.12 | 76     | 5430   |

#### Charts

##### Report R1

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/a47ef467313a4b1a2037b6e33e30c08ca85b60b7ec8dfd35.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/012bbcba1f024d566c3a8dd6b1059e099bdddafcadc0a9f4.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/15ec1a0775d74b8e19ee98eba75d876337b50d4639078612.png)

##### Report R2

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/049bc5f001b563949e0fbb9160d89b65858053ba89c13f18.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/5e2b8c49aa8a85b55c60f2bdecc1799cafaa8299ebec603a.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/c6fbe2ddf7ab3565defe77c58ff8d7166647336edc306588.png)
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

| Report ID | Method ID | Users | RU  | WT          | SGI      | SGI W | Duration | Requests | Fails | RPS | Avg RT | Min RT | Max RT |
|-----------|-----------|-------|-----|-------------|----------|-------|----------|----------|-------|-----|--------|--------|--------|
| R1        | A1        | 100   | 100 | 0.01 - 0.02 | Gunicorn | 25    | 3m       | 159075   | 0     | 909 | 93.01  | 29     | 1160   |

#### Charts

##### Report R1

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/a47ef467313a4b1a2037b6e33e30c08ca85b60b7ec8dfd35.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/012bbcba1f024d566c3a8dd6b1059e099bdddafcadc0a9f4.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/15ec1a0775d74b8e19ee98eba75d876337b50d4639078612.png)
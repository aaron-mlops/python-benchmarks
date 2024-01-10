# fastapi sync vs async

## how to test
### sync
1. run server_sync.py
```shell
python server_sync.py
```
2. run client_test.py
```shell
python client_test.py --num_users 10 --total_requests 100
python client_test.py --num_users 40 --total_requests 400
python client_test.py --num_users 100 --total_requests 1000
```
3. terminate server

### async
1. run server_async.py
```shell
python server_async.py
```
2. run client_test.py
```shell
python client_test.py --num_users 10 --total_requests 100
python client_test.py --num_users 40 --total_requests 400
python client_test.py --num_users 100 --total_requests 1000
```
3. terminate server


## Performance
total time

|               | num user: 10<br/>total requests: 100 | num user: 40<br/>total requests: 400 | num user: 100<br/>total requests: 1000 |
|---------------|--------------------------------------|--------------------------------------|----------------------------------------|
| sync server   | avg: 1.0231<br/>total: 10.24671      | avg: 1.05919<br/>total: 10.63663     | avg: 2.44698<br/>total: 25.34255       |
| async server  | avg: 1.02253<br/>total: 10.2439      | avg: 1.03449<br/>total: 10.39144     | avg: 1.04946<br/>total: 10.65541       |

When number of user is 100, total time of sync server takes 2.5 times becuase fastapi uses 40 threads. (100/40 = 2.5)

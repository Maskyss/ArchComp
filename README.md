# ArchComp

We have two mode:
with server part and without server(only work with json)

Serverpart need some commands in commandline:
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read pages","done":false,"day":"8","month":"11","year":"2019"}' http://localhost:5000/tasks

curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/tasks/1

curl -i http://localhost:5000/tasks/1

curl -X DELETE  http://localhost:5000/tasks/1

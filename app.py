from flask import Flask, request
from rq import Queue
from worker import task_in_background
import redis

app = Flask(__name__)

redis_host = "172.17.0.4"
redis_port = 6379
redis_db = 0

r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
q = Queue(connection=r)

@app.route("/task")  
def add_task():  
 
    if request.args.get("t"):  
 
        job= q.enqueue(task_in_background, request.args.get("t"))  
 
        q_len = len(q)  
 
        return f"The task {job.id} is added into the task queue at {job.enqueued_at}. {q_len} task in the queue"  
    return "Task Queue with Flask"  
 
if __name__ == "__main__":  
    app.run()

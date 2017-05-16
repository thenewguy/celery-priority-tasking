from celery import Celery
from kombu import Exchange, Queue
import time

celery_app = Celery('tasks', backend='amqp', broker='amqp://')

# Creating another queue with priority argument

celery_app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

# celery worker -c 1 -A tasks -Q tasks --loglevel=info
# ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill

# rabbitmqctl stop
# rabbitmq-server -detached

###

# Idea of the sample project is to simulate transcoding of a video into
# different dimensions using celery priority task queues, and actually
# test if it is priority based.

# example: transcode_360p.apply_async(queue='tasks', priority=1)

###


@celery_app.task
def transcode_360p():
    # Simulate transcoding a video into 360p resolution
    print 'BEGIN:   Video transcoding to 360p resolution!'
    time.sleep(5)
    print 'END:   Video transcoded to 360p resolution!'


@celery_app.task
def transcode_480p():
    # Simulate transcoding a video into 480p resolution
    print 'BEGIN:   Video transcoding to 480p resolution!'
    time.sleep(10)
    print 'END:   Video transcoded to 480p resolution!'


@celery_app.task
def transcode_720p():
    # Simulate transcoding a video into 720p resolution
    print 'BEGIN:   Video transcoding to 720p resolution!'
    time.sleep(15)
    print 'END:   Video transcoded to 720p resolution!'


@celery_app.task
def transcode_1080p():
    # Simulate transcoding a video into 1080p resolution
    print 'BEGIN:   Video transcoding to 1080p resolution!'
    time.sleep(20)
    print 'END:   Video transcoded to 1080p resolution!'

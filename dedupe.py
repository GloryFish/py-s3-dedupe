#! /usr/local/bin/python

import boto
conn = boto.connect_s3()

bucket = conn.get_bucket('gloryfish')

etags_seen = dict()

for key in bucket.list('photos'):
  name = key.name.encode('utf-8')
  etag = key.etag.encode('utf-8')
  duplicate = ''

  if etag in etags_seen:
    etags_seen[etag].append(key)
  else:
    etags_seen[etag] = [key]

for etag in [etag for etag in etags_seen.keys() if len(etags_seen[etag]) > 1]:
  print etag.encode('utf-8')
  for key in etags_seen[etag]:
    print "    %s" % (key.name.encode('utf-8'))
  print "\n"
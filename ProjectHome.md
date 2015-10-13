
---


**Notice**: s3funnel is now being maintained on Github. Please refer to this repository: https://github.com/sstoiana/s3funnel


---


**s3funnel** is a command line tool for [Amazon's Simple Storage Service](http://www.amazon.com/gp/browse.html?node=16427261) (S3).

  * Written in Python, `easy_install` the package to install as an egg.
  * Supports multithreaded operations for large volumes. `Put`, `get`, or `delete` many items concurrently, using a fixed-size pool of threads.
  * Built on [workerpool](http://code.google.com/p/workerpool/) for multithreading and [boto](http://code.google.com/p/boto/) for access to the Amazon S3 API.
  * Unix-friendly input and output. Pipe things in, out, and all around.

# Usage #

```
Usage: s3funnel BUCKET OPERATION [OPTIONS] [FILE]...

s3funnel is a multithreaded tool for performing operations on Amazon's S3.

Key Operations:
    DELETE Delete key from the bucket
    GET    Get key from the bucket
    PUT    Put file into the bucket (key corresponds to filename)

Bucket Operations:
    CREATE Create a new bucket
    DROP   Delete an existing bucket (must be empty)
    LIST   List keys in the bucket. If no bucket is given, buckets will be listed.


Options:
  -h, --help            show this help message and exit
  -a AWS_KEY, --aws_key=AWS_KEY
                        Overrides AWS_ACCESS_KEY_ID environment variable
  -s AWS_SECRET_KEY, --aws_secret_key=AWS_SECRET_KEY
                        Overrides AWS_SECRET_ACCESS_KEY environment variable
  -t N, --threads=N     Number of threads to use [default: 1]
  -T SECONDS, --timeout=SECONDS
                        Socket timeout time, 0 is never [default: 0]
  --start_key=KEY       (`list` only) Start key for list operation
  --acl=ACL             (`put` only) Set the ACL permission for each file
                        [default: public-read]
  -i FILE, --input=FILE
                        Read one file per line from a FILE manifest.
  -v, --verbose         Enable verbose output. Use twice to enable debug
                        output.
```

# Examples #

Note: Appending the `-v` flag will print useful progress information to stderr. Great for learning the tool.

```
$ s3funnel mybukkit create
$ s3funnel list
mybukkit
$ touch 1 2 3
$ s3funnel mybukkit put 1 2 3
$ s3funnel mybukkit list
1
2
3
$ rm 1 2 3
$ s3funnel mybukkit get 1 2 3 --threads=2
$ ls -1
1
2
3
$ s3funnel mybukkit list | s3funnel mybukkit delete
$ s3funnel mybukkit list
$ s3funnel mybukkit drop
$ s3funnel list
```
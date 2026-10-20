### What Is This

This is the implementation of an AWS Lambda Function which is defined in the https://github.com/ahsanjkhan/MathPracsStarterDemoCDK repository.

The purpose of this Lambda is to list the files in the starter demo S3 bucket.

You can learn more about MathPracs at https://mathpracs.com

### How Does It Work

The Lambda is invoked by an AWS EventBridge Scheduler Rule every 100 minutes.

It lists every object in the S3 bucket named by the `BUCKET_NAME` environment variable, prints the file count and names to CloudWatch Logs, and returns them as JSON.

### What Are The Components

AWS Lambda, AWS S3, AWS EventBridge Scheduler.

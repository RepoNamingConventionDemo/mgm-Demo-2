# main.tf
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"          # Example Access Key
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Example Secret Key
}

resource "aws_s3_bucket" "example" {
  bucket = "my-test-bucket-123456"
  acl    = "private"
}

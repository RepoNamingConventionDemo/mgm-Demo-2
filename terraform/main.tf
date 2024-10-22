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

# main.tf
provider "aws" {
  region     = "us-west-2"
  access_key = "AKIAIOSFODNN7EXAMPLE"          # Example Access Key
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Example Secret Key
}

resource "aws_db_instance" "example" {
  identifier         = "test-db"
  engine             = "mysql"
  instance_class     = "db.t2.micro"
  allocated_storage   = 20
  username           = "admin"                    # Example Username
  password           = "P@ssw0rd123"              # Example Password
  db_subnet_group_name = aws_db_subnet_group.example.name
}

resource "aws_db_subnet_group" "example" {
  name       = "test-subnet-group"
  subnet_ids = ["subnet-12345678", "subnet-87654321"]

  tags = {
    Name = "My DB Subnet Group"
  }
}

# main.tf
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"          # Example Access Key
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Example Secret Key
}

resource "aws_api_gateway_rest_api" "example" {
  name        = "example-api"
  description = "Example API Gateway"
  api_key_source = "HEADER"
}

resource "aws_api_gateway_api_key" "example" {
  name        = "example-api-key"
  description = "Example API Key"
  enabled     = true
  value       = "example-api-key-value"  # Example API Key Value
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true
  endpoints {
    s3        = "http://localhost:4566"
    dynamodb  = "http://localhost:4566"
    ec2       = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "mi_bucket" {
  bucket        = "lab-bucket-local"
  force_destroy = true
}

resource "aws_dynamodb_table" "mi_tabla" {
  name         = "lab-table-local"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_instance" "mi_instancia" {
  ami           = "ami-12345678" # valor ficticio para Localstack
  instance_type = "t2.micro"
}
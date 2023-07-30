import os

def main():
  print("Hello From GitHub Actions!")
  token = os.environ.get("MY_SECRET_TOKEN")
  if not token:
    raise RuntimeError("MY_SECRET_TOKEN env var is not set!")
  print("All good! we found our env var!")
  

if __name__ == '__main__':
  main()

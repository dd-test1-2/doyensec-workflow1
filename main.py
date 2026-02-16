from render_sdk.workflows import task, start
import asyncio

# A basic task
@task
def calculate_square(a: int) -> int:
  return a * a

# A task that runs two subtasks in parallel
@task
async def sum_squares(a: int, b: int) -> int:
  result1, result2 = await asyncio.gather(
    calculate_square(a),
    calculate_square(b)
  )
  return result1 + result2

@task
async def read_file(path: str) -> str:
  with open(path) as file:
    return file.read()

if __name__ == "__main__":
  start() # SDK entry point


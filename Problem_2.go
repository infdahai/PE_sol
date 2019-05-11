package main

import "fmt"

func main() {
/*
  limit := 4000000
  cache := []int{1,1}

  next_val := 0
  even_fib := 0
  for next_val < limit{
    next_val = cache[0] + cache[1]
    cache[0],cache[1] = cache[1],next_val
    if next_val %2 == 0 {
      if next_val < limit {
        even_fib += next_val
      }
    }
  }
  fmt.Println(even_fib)
 */
   limit := 4000000
  cache := []int{2,8}

  next_val := 0
  even_fib := 10
  for next_val<limit{
    even_fib += next_val
    next_val = 4*cache[1]+cache[0]
    cache[0],cache[1] = cache[1],next_val
  }
  fmt.Println(even_fib)
}

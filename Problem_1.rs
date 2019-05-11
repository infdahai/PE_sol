//  1+2+3+...+p=½*p*(p+1) 
// the exact and quick sol is : SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)
// I should use this sol as the first idea.

// still a Rust freshman,  so just copy the rust code from https://projecteuler.net/thread=1;page=9#last

use ferris_says::say;
use std::io::{stdout,BufWriter};

fn sum_multiples(n:i32,from: i32,to:i32)->i64{
    let k = if to%n==0{
        (to-1)/n
    }else{
        to/n 
    };
    let j = from/n;
    ((k*(k+1)-j*(j+1))/2*n) as i64
}
fn p001() -> i64{
    let (from,to) = (0,1000);
    sum_multiples(3,from,to)+ sum_multiples(5, from, to) - sum_multiples(15, from, to)
}

fn main() {
    let stdout = stdout();
    let out = format!("{}",p001());
    let width = 24;
    let mut writer = BufWriter::new(stdout.lock());
    say(out.as_bytes(),width,&mut writer).unwrap();
}

/** I am a freshman in Kotlin. And I paste the code from my hand and just enhance my ability in KT */
/**ref_link: https://projecteuler.net/thread=2;page=8*/

fun main(){
  val goldenRatio = 1.618034
  var sum: Long =  0
  var term = 2.0
  while(true){
   val fbn = ((Math.pow(goldenRatio,term)-Math.pow(1-goldenRatio,term))/Math.sqrt(5.0)).toLong()
   if (fbn>4000000) {break}
   if(fbn%2L==0L){sum+=fbn}
   ++term
  }
  print("sum:$sum")
}

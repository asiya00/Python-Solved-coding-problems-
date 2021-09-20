import java.util.stream.IntStream;
import java.util.stream.Stream;
class HackerEarth
{
    public static void main(String args[])
{
Stream<double[]>HackValue=IntStream.rangeClosed(1,100)
.boxed().flatMap(a->IntStream.rangeClosed(a,10)
.mapToObj(
b->new double[]{a,b,Math.sqrt(a*a+b*b)})
.filter(t->t[2]%1==0));

HackValue.limit(5)
.forEach(t->System.out.println(t[0]+","+t[1]+','+t[2]));
}
}
// 3.0,4.0,5.0
// 6.0,8.0,10.0
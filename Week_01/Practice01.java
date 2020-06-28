import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;

public class Practice01 {
    public static void main(String[] args) {
        Deque<String> deque = new LinkedList<String>();
        deque.addFirst("a");
        deque.addFirst("b");
        deque.addFirst("c");
        System.out.println("deque的元素有："+deque);
        Iterator<String> i = deque.iterator();
        System.out.println(i.next());
        System.out.println(deque.contains("a"));

        String str = deque.getFirst();
        System.out.println("获取deque的栈顶："+str);
        System.out.println("deque的元素有："+deque);

        while (deque.size()>0) {
            System.out.println("出栈："+deque.removeFirst());
        }
        System.out.println("deque的元素此时有："+deque);
    }
}

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	private static int x; // 원
	private static int y; // 그램
	private static int n; // 편의점 개수
	private static double min = 0; // 1000그램 가격의 최저가
	
    public static void main(String[] args) throws IOException { // BufferedReader 사용할 때 IO 예외처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 문자열 입력
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(br.readLine());
        min = (1000 * x) / (double)y;
        
        int tx;
        int ty;
        
        for (int i = 0; i < n; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	tx = Integer.parseInt(st.nextToken());
        	ty = Integer.parseInt(st.nextToken());
        	min = Double.compare((1000 * tx) / (double)ty, (double)min) < 0 ? (1000 * tx) / (double)ty: (double)min;
        }
        
        System.out.println(min);
    }
    
}
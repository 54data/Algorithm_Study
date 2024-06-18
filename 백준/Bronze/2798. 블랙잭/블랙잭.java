import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int n; // 카드 개수
    private static int m; // 가까워져야 하는 값
    private static boolean[] visited; // 방문 처리 확인
    private static int[] cardAry; // 카드 배열
    private static int max = 0; // 카드 3장 최대합
    
    public static void main(String[] args) throws IOException { // BufferedReader 사용할 때 IO 예외처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 문자열 입력
        StringTokenizer st = new StringTokenizer(br.readLine(), " "); // 공백을 기준으로 나누기
        n = Integer.parseInt(st.nextToken()); // 나눠진 문자열을 정수로 변환하여 변수 초기화
        m = Integer.parseInt(st.nextToken());
        visited = new boolean[n];
        cardAry = new int[n];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < cardAry.length; i++) {
            cardAry[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0, 0);
        System.out.println(max);
    }

    public static void dfs(int cnt, int sum) {
        if (cnt == 3) {
            if (sum <= m) { 
                max = Math.max(sum, max); 
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(cnt + 1, sum + cardAry[i]);
                visited[i] = false;
            }
        }
    }
}
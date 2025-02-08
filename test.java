import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- != 0) {
            int n = scanner.nextInt();
            HashMap<Integer, Integer> map = new HashMap<>();

            for (int i = 0; i < n; i++) {
                int val = scanner.nextInt();
                map.put(val, map.getOrDefault(val, 0) + 1);
            }

            int row = 0, col = 0;
            for (int i = 1; i <= 200000; i++) {
                if (map.containsKey(i)) {
                    int rowCount = map.get(i);
                    int div = n / i;
                    int rem = n % i;

                    if (rem == 0 && map.containsKey(div)) {
                        int colCount = map.get(div);
                        if (i == div) {
                            if (colCount >= 2) {
                                row = col = div;
                                break;
                            }
                        } else {
                            row = div;
                            col = i;
                            break;
                        }
                    }
                }
            }
            System.out.println(row + " " + col);
        }
        scanner.close();
    }
}

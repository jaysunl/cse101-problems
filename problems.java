import java.util.*;
import java.io.*;

public class problems {

    static Comparator<Integer[]> LampComparator = Comparator.comparing(i -> i[1]);

    public static long minCost(int H, List<Integer[]> L /* int[][] list */) {
        /**
         * for j = 0, . . . , n
         * (2) M[0, j] = 0
         * (3) for i = 1, . . . , n
         * (4) M[i, 0] = ∞
         * (5) for i = 1, . . . , n
         * (6) for j = 1, . . . , n
         * (7) if j − A[j] ≤ i ≤ j + A[j]:
         * (8) rb = max(j − A[j] − 1, 0)
         * (9) M[i, j] = min(M[i, j − 1], A[j] + M[rb, j − 1])
         * (10) else M[i, j] = M[i, j − 1]
         * (11) return M[n, n]
         */
        // i = houses, j = lamps
        // L.add(new Integer[] { 0, 0, 0 });
        L.sort(LampComparator);
        // Collections.reverse(L);
        for (Integer[] integers : L) {
            System.out.println(Arrays.asList(integers));
        }

        long[][] dp = new long[L.size() + 1][H + 1];
        for (int i = 1; i < dp.length; i++) {
            dp[i][0] = (long) 0;
        }
        for (int j = 1; j < dp[0].length; j++) {
            dp[0][j] = (long) Integer.MAX_VALUE;

        }

        for (int i = 1; i < dp.length; i++) { // lamps
            for (int j = 1; j < dp[0].length; j++) { // houses

                if (L.get(i - 1)[1] < j) {
                    dp[i][j] = (long) Integer.MAX_VALUE;
                } else if (L.get(i - 1)[0] > j) {
                    dp[i][j] = dp[i - 1][j];

                } else {
                    dp[i][j] = Math.min(dp[i - 1][j], L.get(i - 1)[2] + dp[i - 1][(L.get(i - 1)[0]) - 1]);
                }

                // System.out.print(dp[i - 1][j]);
                // System.out.print(" ");
                // System.out.println(L.get(i - 1)[2] + dp[i - 1][L.get(i - 1)[0] - 1]);

                // System.out.print(dp[i][j] + " ");
                // System.out.print(String.join(" ", String.valueOf(i), " ", String.valueOf(j),
                // " "));
            }
            // System.out.println("");
        }

        // for (int i = 0; i < dp.length; i++) {
        // System.out.println("");
        // for (int j = 0; j < dp[0].length; j++) {
        // System.out.print(dp[i][j] + " ");
        // }
        // }
        return dp[dp.length - 1][dp[0].length - 1];
    }

    public static void main(String[] args) throws Exception {
        /*
         * char[] C = {'N', 'H', 'N', 'M', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'N'};
         * long val = findMin(C);
         */
        int H = 5;
        List<Integer[]> L = new ArrayList<>();
        L.add(new Integer[] { 1, 3, 2 });
        L.add(new Integer[] { 2, 4, 4 });
        L.add(new Integer[] { 2, 5, 8 });
        L.add(new Integer[] { 4, 5, 3 });
        long val = minCost(H, L);
        System.out.println(val);

        List<Integer[]> myList = new ArrayList<>();

        // for (int j = 0; j <= 2000; j++) {
        // myList.add(new Integer[3]);
        // }

        // C:\\Users\\Dice\\IdeaProjects\\tests\\streetlamps.csv
        try {
            // Scanner sc = new Scanner(new
            // File("C:\\Users\\Dice\\IdeaProjects\\tests\\streetlamps.csv"));

            // sc.useDelimiter("\\n|,"); // sets the delimiter pattern
            // int count = 0;
            // int i = 0;
            // while (sc.hasNext()) // returns a boolean value
            // {
            // myList.add(new Integer[3]);
            // if (count == 3) {
            // count = 0;
            // i++;
            // // sc.nextLine();
            // // System.out.println("");
            // }

            // myList.set(count,Integer.parseInt(sc.next().replaceAll("[^0-9]+", ""));
            // // System.out.print(myList.get(i)[count]);

            // count++;
            // // System.out.print(sc.next()); // find and returns the next complete token
            // // from
            // // this scanner
            // }
            // // long min = minCost(2000, myList);
            // // System.out.println(min);
            // sc.close(); // closes the scanner

            String line = "";
            String splitBy = ",";

            BufferedReader br = new BufferedReader(new FileReader("streetlamps_82.csv"));
            while ((line = br.readLine()) != null) // returns a Boolean value
            {
                String[] lamp = line.split(splitBy);
                Integer[] intArray = new Integer[3];
                for (int i = 0; i < lamp.length; i++) {
                    intArray[i] = Integer.parseInt(lamp[i]);
                }

                myList.add(intArray);
            }

            // for (Integer[] integers : myList) {
            // System.out.println(Arrays.asList(integers));
            // }

            // System.out.println(myList.size());

            int houses = 2000;
            long value = minCost(houses, myList);
            System.out.println(value);

            br.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
package main.java.app;
import java.io.OutputStream;

import java.net.HttpURLConnection;
import java.net.URL;

public class Client {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://localhost:5000/predict");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInputString = "{\"age\": 28, \"income\": 20000, \"loanAmount\": 40000}";


            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            java.util.Scanner scanner = new java.util.Scanner(conn.getInputStream());
            while (scanner.hasNext()) {
                System.out.println(scanner.nextLine());
            }
            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

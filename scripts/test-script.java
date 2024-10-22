// SecretsTest.java
public class SecretsTest {
    // Intentionally exposing a database password
    private static final String DB_PASSWORD = "P@ssw0rd!123"; // Example secret

    public static void main(String[] args) {
        connectToDatabase();
    }

    private static void connectToDatabase() {
        System.out.println("Connecting to database with password: " + DB_PASSWORD);
    }
}

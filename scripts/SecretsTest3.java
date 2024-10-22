// SecretsTest3.java
public class SecretsTest3 {
    // Intentionally exposing a hardcoded password
    private static final String PASSWORD = "mySecretP@ssw0rd"; // Example password

    public static void main(String[] args) {
        login();
    }

    private static void login() {
        System.out.println("Logging in with password: " + PASSWORD);
    }
}


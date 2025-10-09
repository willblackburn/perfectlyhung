// Import CSS for Vite HMR
import "../css/main.css";

// Enable HMR for CSS
if (import.meta.hot) {
  import.meta.hot.accept("../css/main.css", () => {
    console.log("CSS updated");
  });
}

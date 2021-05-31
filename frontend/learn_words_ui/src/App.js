import Layout from "./components/Layout";
import "./css/App.css";
import Urls from "./Urls";

function App() {
  return (
    <div className="App">
      <Layout>
        <Urls />
      </Layout>
    </div>
  );
}

export default App;

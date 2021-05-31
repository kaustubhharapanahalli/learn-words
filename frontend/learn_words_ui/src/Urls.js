import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Home from "./components/Home";

function Urls(props) {
  return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <Home {...props} />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default Urls;

import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import CssBaseline from "@material-ui/core/CssBaseline";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";

const useStyles = makeStyles((theme) => ({
  footer: {
    padding: theme.spacing(3, 2),
    marginTop: "auto",
    backgroundColor:
      theme.palette.type === "light"
        ? theme.palette.grey[200]
        : theme.palette.grey[800],
  },
}));

function Layout(props) {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Header {...props} />
      <div>{props.children}</div>
      <footer className={classes.footer}>
        <Container maxWidth="sm">
          <Footer />
        </Container>
      </footer>
    </React.Fragment>
  );
}

export default Layout;

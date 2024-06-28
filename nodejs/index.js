var pjson = require("./package.json");
const os = require("os");
const express = require("express");
const app = express();
app.set("view engine", "ejs");
const port = 3000;
const BEARER_TOKEN = "ghp_SEcreTS3gOh2VfulanoyDtjmEITAT012345";

app.get("/", (req, res) => {
  res.render("index", {
    applicationVersion: pjson.version,
    hostAddress: req.ip,
    hostName: os.hostname(),
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

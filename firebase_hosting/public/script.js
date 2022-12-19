//import firebase from "firebase/app"
import { getRemoteConfig } from "firebase/remote-config";
import { getStorage } from "firebase/storage"
import { getDatabase } from "firebase/database"
import { getHosting } from "firebase/hosting"
import dotenv from "dotenv";
import { env } from 'node:process';

//.env ファイルの内容を読み込
//require('dotenv').config({path: '.env'});
//const functions = require('firebase-functions');
//require('dotenv').config()

const firebaseConfig = {
  //apiKey: process.env.apiKey,
    //authDomain: "process.env.authDomain",
  APIKEY: "process.env.APIKEY",
  authDomain: "process.env.AUTHDOMAIN",
  databaseURL: "process.env.DATABASEURL",
  projectId: "process.env.PROJECTID",
  storageBucket: "process.env.STORAGEBUCKET",
  messagingSenderId: "process.env.MESSAGINGSENDERID",
  appId: "process.env.APPID"
 };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");

// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
snapshot.forEach(function(childSnapshot) {
  const image = childSnapshot.val()["image"];
  const time = childSnapshot.val()["timestamp"];
  const storageRef = storage.ref(image);

  storageRef
    .getDownloadURL()
    .then(function(url) {
      console.log(url);
      document.getElementById("photo").src = url;
      document.getElementById("time").innerText = time;
    })
    .catch(function(error) {
      console.log(error);
    });
});
});
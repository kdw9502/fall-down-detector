package org.tensorflow.lite.examples.posenet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpMgrThread extends Thread{
    HttpMgrThread(){
    }
    @Override
    public void run(){
        try {
            ssock();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void ssock() throws IOException {
        BufferedReader in = null;
        try {
            //URL url = new URL("http://18.233.171.252:8000");
            URL url = new URL("https://j7wfx9pqy1.execute-api.us-east-1.amazonaws.com/fall-down/alert?user_id=cmc");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            in = new BufferedReader(new InputStreamReader(con.getInputStream(), "UTF-8"));

        } catch(Exception e){
            e.printStackTrace();
        }
    }
}

package org.tensorflow.lite.examples.posenet;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.util.Log;
import androidx.preference.PreferenceManager;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpMgrThread extends Thread{
    private Context context;
    HttpMgrThread(Context context){
        this.context = context;
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

            String base_url = "https://j7wfx9pqy1.execute-api.us-east-1.amazonaws.com/fall-down/alert?phone_number=%s";
            SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(context);
            String phone_number = preferences.getString("phone_number","");

            Log.d("test",phone_number);

            if (phone_number.isEmpty())
                return;

            URL url = new URL(String.format(base_url,phone_number));
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            in = new BufferedReader(new InputStreamReader(con.getInputStream(), "UTF-8"));


        } catch(Exception e){
            e.printStackTrace();
        }
    }
}

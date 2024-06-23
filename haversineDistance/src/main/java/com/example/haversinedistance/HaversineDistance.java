/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.example.haversinedistance;

import ai.rapids.cudf.ColumnVector;
import com.nvidia.spark.RapidsUDF;
import org.apache.spark.sql.api.java.UDF4;

public class HaversineDistance implements UDF4<Double, Double, Double, Double, Double>, RapidsUDF {

    // Native method declaration for columnar processing
    private native long computeHaversine(long lat1Addr, long lon1Addr, long lat2Addr, long lon2Addr);

    @Override
    public Double call(Double lat1, Double lon1, Double lat2, Double lon2) {
        final int R = 6371; // Radius of the Earth in kilometers
        double latDistance = Math.toRadians(lat2 - lat1);
        double lonDistance = Math.toRadians(lon2 - lon1);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                + Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        double distance = R * c; // Convert to kilometers

        return distance;
    }

    @Override
    public ColumnVector evaluateColumnar(int numRows, ColumnVector... args) {
        UDFNativeLoader.ensureLoaded();
        ColumnVector lat1 = args[0];
        ColumnVector lon1 = args[1];
        ColumnVector lat2 = args[2];
        ColumnVector lon2 = args[3];
        long nativeResult = computeHaversine(lat1.getNativeView(), lon1.getNativeView(), lat2.getNativeView(), lon2.getNativeView());
        return new ColumnVector(nativeResult);
    }
}

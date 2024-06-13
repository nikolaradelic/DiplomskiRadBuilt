/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.example.haversinedistance;

import ai.rapids.cudf.ColumnVector;
import com.nvidia.spark.RapidsUDF;
import org.apache.spark.sql.api.java.UDF4;

public class HaversineDistance implements UDF4<double[], double[], double[], double[], double[]>, RapidsUDF {

    // Native method declaration for columnar processing
    private native long computeHaversine(long lat1Addr, long lon1Addr, long lat2Addr, long lon2Addr, int length);

    @Override
    public double[] call(double[] lat1, double[] lon1, double[] lat2, double[] lon2) {
        throw new UnsupportedOperationException("This UDF should only be used for columnar processing");
    }

    @Override
    public ColumnVector evaluateColumnar(int numRows, ColumnVector... args) {
        UDFNativeLoader.ensureLoaded();
        ColumnVector lat1 = args[0];
        ColumnVector lon1 = args[1];
        ColumnVector lat2 = args[2];
        ColumnVector lon2 = args[3];
        int length = (int) lat1.getRowCount();
        long nativeResult = computeHaversine(lat1.getNativeView(), lon1.getNativeView(), lat2.getNativeView(), lon2.getNativeView(), length);
        return new ColumnVector(nativeResult);
    }
}

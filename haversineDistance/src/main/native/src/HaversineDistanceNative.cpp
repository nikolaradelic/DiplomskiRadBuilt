#include <jni.h>
#include <cuspatial/distance/haversine.hpp>
#include <memory>
#include <cudf/column/column.hpp>
#include <cudf/column/column_view.hpp>

extern "C" {
    JNIEXPORT jlong JNICALL Java_com_example_haversinedistance_HaversineDistance_computeHaversine
      (JNIEnv* env, jclass, jlong lat1Addr, jlong lon1Addr, jlong lat2Addr, jlong lon2Addr, jint length) {

        auto lat1_col = reinterpret_cast<cudf::column_view const*>(lat1Addr);
        auto lon1_col = reinterpret_cast<cudf::column_view const*>(lon1Addr);
        auto lat2_col = reinterpret_cast<cudf::column_view const*>(lat2Addr);
        auto lon2_col = reinterpret_cast<cudf::column_view const*>(lon2Addr);

        // Compute the Haversine distance
        auto distances = cuspatial::haversine_distance(
            *lat1_col, *lon1_col, *lat2_col, *lon2_col);

        // Return the native pointer to the new column
        return reinterpret_cast<jlong>(distances.release());
    }
}

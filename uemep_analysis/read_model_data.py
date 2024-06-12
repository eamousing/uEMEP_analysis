import xarray as xr
import cartopy.crs as ccrs
import gc


def read_netcdf(file):
    ds = xr.open_dataset(file)
    lon = xr.DataArray(ds["lon"])
    lat = xr.DataArray(ds["lat"])
    pm25 = xr.DataArray(ds["pm25_concentration"]).isel(time=0)
    
    proj_vars = ds["projection_ETRS89_LAEA"]
    projection = ccrs.LambertAzimuthalEqualArea(
        central_longitude=proj_vars.longitude_of_projection_origin,
        central_latitude=proj_vars.latitutde_of_projection_origin,
        false_easting=proj_vars.false_easting,
        false_northing=proj_vars.false_northing
    )

    # Manually close and delete to preserve memory
    ds.close()
    del ds
    gc.collect()

    # Return as dictonary
    return {"Longitude": lon, "Latitude": lat, "PM2.5": pm25, "Projection": projection}

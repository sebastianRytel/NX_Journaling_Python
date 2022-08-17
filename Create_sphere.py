import NXOpen

the_session = NXOpen.Session.GetSession()
parts = the_session.Parts
work_part = parts.Work
listing_window = the_session.ListingWindow

dummy_sphere = NXOpen.Features.Sphere.Null

builder = work_part.Features.CreateSphereBuilder(dummy_sphere)
builder.Type = NXOpen.Features.SphereBuilder.Types.CenterPointAndDiameter

p1 = NXOpen.Point3d(0.0, 0.0, 0.0)
pt1 = work_part.Points.CreatePoint(p1)

builder.CenterPoint = pt1
builder.Diameter.RightHandSide = str(3)
builder.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

builder.Commit()
builder.Destroy()

from pykinect.nui import JointId

MANO_IZQ = (JointId.ShoulderCenter,
            JointId.ShoulderLeft,
            JointId.ElbowLeft,
            JointId.WristLeft,
            JointId.HandLeft)
MANO_DER = (JointId.ShoulderCenter,
            JointId.ShoulderRight,
            JointId.ElbowRight,
            JointId.WristRight,
            JointId.HandRight)
PIE_IZQ  = (JointId.HipCenter,
            JointId.HipLeft,
            JointId.KneeLeft,
            JointId.AnkleLeft,
            JointId.FootLeft)
PIE_DER  = (JointId.HipCenter,
            JointId.HipRight,
            JointId.KneeRight,
            JointId.AnkleRight,
            JointId.FootRight)
ESPINA = (JointId.HipCenter,
          JointId.Spine,
          JointId.ShoulderCenter,
          JointId.Head)

# SKULL = (MANO_DER, MANO_IZQ, PIE_DER, PIE_IZQ, ESPINA)
SKULL = {'mano derecha':MANO_DER,
         'mano izquierda':MANO_IZQ,
         'pie derecho':PIE_DER,
         'pie izquierdo':PIE_IZQ,
         'espina':ESPINA}
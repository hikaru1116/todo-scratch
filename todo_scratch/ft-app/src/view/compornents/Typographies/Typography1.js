import React from "react";
import Typography from "@mui/material/Typography";

const Typography1 = ({ color, children }) => {
  const typoColor = color != null ? color : "#111111";

  return (
    <Typography fontSize={24} sx={{ color: typoColor }}>
      {children}
    </Typography>
  );
};

export default Typography1;

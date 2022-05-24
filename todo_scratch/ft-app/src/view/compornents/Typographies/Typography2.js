import React from "react";
import Typography from "@mui/material/Typography";

const Typography2 = ({ color, children }) => {
  const typoColor = color != null ? color : "#111111";

  return (
    <Typography fontSize={20} sx={{ color: typoColor }}>
      {children}
    </Typography>
  );
};

export default Typography2;

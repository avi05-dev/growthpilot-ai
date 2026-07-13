import { Card, CardContent } from '@mui/material';
import type { CardProps } from '@mui/material/Card';
import type { PropsWithChildren } from 'react';

export function DashboardCard({ children, sx, ...props }: PropsWithChildren<CardProps>) {
  return (
    <Card sx={{ height: '100%', ...(sx as object) }} {...props}>
      <CardContent sx={{ p: { xs: 2.5, md: 3 }, '&:last-child': { pb: { xs: 2.5, md: 3 } } }}>{children}</CardContent>
    </Card>
  );
}

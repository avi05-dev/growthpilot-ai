import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import BoltIcon from '@mui/icons-material/Bolt';
import PaidIcon from '@mui/icons-material/Paid';
import PeopleAltIcon from '@mui/icons-material/PeopleAlt';
import QueryStatsIcon from '@mui/icons-material/QueryStats';
import { Box, Button, Card, CardContent, Chip, Grid, LinearProgress, Stack, Typography } from '@mui/material';
import type { ReactNode } from 'react';

type DashboardPageProps = {
  pageTitle?: string;
};

type MetricCard = {
  label: string;
  value: string;
  delta: string;
  helper: string;
  icon: ReactNode;
};

const metricCards: MetricCard[] = [
  { label: 'Qualified pipeline', value: '$428K', delta: '+18.4%', helper: 'vs. last month', icon: <PaidIcon /> },
  { label: 'Active audiences', value: '24.8K', delta: '+12.7%', helper: 'high-intent users', icon: <PeopleAltIcon /> },
  { label: 'Campaign velocity', value: '91%', delta: '+8.2%', helper: 'on-track experiments', icon: <BoltIcon /> },
  { label: 'Signal confidence', value: '87', delta: '+5 pts', helper: 'AI model score', icon: <QueryStatsIcon /> },
];

const growthPlays = [
  'Launch lifecycle nurture for dormant product-qualified leads.',
  'Increase LinkedIn spend on the enterprise operations audience.',
  'Route high-fit trial accounts to sales within eight minutes.',
];

export function DashboardPage({ pageTitle = 'Dashboard' }: DashboardPageProps) {
  return (
    <Stack spacing={4}>
      <Stack direction={{ xs: 'column', md: 'row' }} spacing={2} justifyContent="space-between" alignItems={{ md: 'center' }}>
        <Box>
          <Chip label="GrowthPilot AI v0.1.0" color="primary" variant="outlined" sx={{ mb: 1.5 }} />
          <Typography variant="h4">{pageTitle}</Typography>
          <Typography color="text.secondary" sx={{ mt: 1 }}>
            Monitor acquisition, activation, and revenue signals from a single AI-powered command center.
          </Typography>
        </Box>
        <Button variant="contained" size="large">
          Generate growth brief
        </Button>
      </Stack>

      <Grid container spacing={3}>
        {metricCards.map((card) => (
          <Grid key={card.label} item xs={12} sm={6} xl={3}>
            <Card>
              <CardContent>
                <Stack direction="row" justifyContent="space-between" alignItems="flex-start">
                  <Box>
                    <Typography variant="body2" color="text.secondary" fontWeight={700}>
                      {card.label}
                    </Typography>
                    <Typography variant="h4" sx={{ mt: 1 }}>
                      {card.value}
                    </Typography>
                  </Box>
                  <Box sx={{ bgcolor: 'primary.light', color: 'primary.contrastText', borderRadius: 3, p: 1.25 }}>{card.icon}</Box>
                </Stack>
                <Stack direction="row" spacing={0.75} alignItems="center" sx={{ mt: 2 }}>
                  <ArrowUpwardIcon color="success" fontSize="small" />
                  <Typography color="success.main" fontWeight={800}>
                    {card.delta}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {card.helper}
                  </Typography>
                </Stack>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Grid container spacing={3}>
        <Grid item xs={12} lg={8}>
          <Card sx={{ height: '100%' }}>
            <CardContent>
              <Typography variant="h6">Revenue momentum</Typography>
              <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
                Placeholder trend module prepared for analytics integration.
              </Typography>
              <Stack spacing={2.5} sx={{ mt: 4 }}>
                {['Acquisition', 'Activation', 'Expansion'].map((label, index) => (
                  <Box key={label}>
                    <Stack direction="row" justifyContent="space-between" sx={{ mb: 1 }}>
                      <Typography fontWeight={700}>{label}</Typography>
                      <Typography color="text.secondary">{[78, 64, 86][index]}%</Typography>
                    </Stack>
                    <LinearProgress variant="determinate" value={[78, 64, 86][index]} sx={{ height: 10, borderRadius: 999 }} />
                  </Box>
                ))}
              </Stack>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} lg={4}>
          <Card sx={{ height: '100%' }}>
            <CardContent>
              <Typography variant="h6">Recommended growth plays</Typography>
              <Stack spacing={2} sx={{ mt: 3 }}>
                {growthPlays.map((play, index) => (
                  <Box key={play} sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 3, p: 2 }}>
                    <Typography variant="caption" color="primary" fontWeight={800}>
                      PLAY {index + 1}
                    </Typography>
                    <Typography sx={{ mt: 0.75 }}>{play}</Typography>
                  </Box>
                ))}
              </Stack>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Stack>
  );
}

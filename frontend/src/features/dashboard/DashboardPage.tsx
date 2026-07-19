import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import CachedIcon from '@mui/icons-material/Cached';
import SourceIcon from '@mui/icons-material/Source';
import { Alert, Box, Button, Chip, FormControl, Grid, InputLabel, MenuItem, Select, Stack, Typography } from '@mui/material';
import { useMutation } from '@tanstack/react-query';
import { useState } from 'react';

import { WorkspaceApi, type WorkspaceGenerateRequest } from '../../api/workspaceApi';
import { DashboardCard } from './components/DashboardCard';
import { HeroHeader } from './components/HeroHeader';
import { SectionHeader } from './components/SectionHeader';
import { DashboardSkeleton, EmptyState } from './components/StateBlock';

const domains = [{ value: 'technology', label: 'Technology' }];
const goals = [{ value: 'career_growth', label: 'Career Growth' }];
const timeWindows = [
  { value: '24h', label: 'Last 24 hours' },
  { value: '7d', label: 'Last 7 days' },
];

export function DashboardPage() {
  const [request, setRequest] = useState<WorkspaceGenerateRequest>({ domain: 'technology', goal: 'career_growth', time_window: '24h' });
  const workspaceMutation = useMutation({ mutationFn: WorkspaceApi.generate });

  const generate = () => workspaceMutation.mutate(request);
  const intelligence = workspaceMutation.data;

  return (
    <Stack spacing={{ xs: 3, md: 4 }}>
      <HeroHeader onRefresh={generate} />

      <DashboardCard>
        <Stack spacing={3}>
          <SectionHeader eyebrow="Agent Workspace" title="Generate Intelligence" description="Planner and Knowledge agents produce cache-aware workspace intelligence from configured providers." />
          <Grid container spacing={2.5}>
            <Grid item xs={12} md={4}>
              <FormControl fullWidth>
                <InputLabel id="domain-label">Domain</InputLabel>
                <Select labelId="domain-label" label="Domain" value={request.domain} onChange={(event) => setRequest((current) => ({ ...current, domain: event.target.value }))}>
                  {domains.map((domain) => (
                    <MenuItem key={domain.value} value={domain.value}>
                      {domain.label}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={12} md={4}>
              <FormControl fullWidth>
                <InputLabel id="goal-label">Goal</InputLabel>
                <Select labelId="goal-label" label="Goal" value={request.goal} onChange={(event) => setRequest((current) => ({ ...current, goal: event.target.value }))}>
                  {goals.map((goal) => (
                    <MenuItem key={goal.value} value={goal.value}>
                      {goal.label}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={12} md={4}>
              <FormControl fullWidth>
                <InputLabel id="time-window-label">Time Window</InputLabel>
                <Select labelId="time-window-label" label="Time Window" value={request.time_window} onChange={(event) => setRequest((current) => ({ ...current, time_window: event.target.value }))}>
                  {timeWindows.map((timeWindow) => (
                    <MenuItem key={timeWindow.value} value={timeWindow.value}>
                      {timeWindow.label}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
          </Grid>
          <Button variant="contained" size="large" startIcon={<AutoAwesomeIcon />} onClick={generate} disabled={workspaceMutation.isPending}>
            {workspaceMutation.isPending ? 'Generating…' : 'Generate Intelligence'}
          </Button>
        </Stack>
      </DashboardCard>

      {workspaceMutation.isPending ? <DashboardSkeleton /> : null}
      {workspaceMutation.isError ? <Alert severity="error">Unable to generate workspace intelligence. Please try again.</Alert> : null}
      {!workspaceMutation.isPending && !workspaceMutation.isError && !intelligence ? <EmptyState title="No intelligence generated yet" description="Choose your workspace inputs and run the agent workflow to generate fresh intelligence." /> : null}

      {intelligence ? (
        <Stack spacing={3}>
          <DashboardCard>
            <Stack spacing={2}>
              <Stack direction="row" spacing={1} alignItems="center">
                <Chip icon={<CachedIcon />} label={intelligence.cache_hit ? 'Cache hit' : 'Fresh generation'} color={intelligence.cache_hit ? 'success' : 'secondary'} />
                <Typography variant="body2" color="text.secondary">
                  Generated {new Date(intelligence.generated_at).toLocaleString()} · Expires {new Date(intelligence.expires_at).toLocaleString()}
                </Typography>
              </Stack>
              <Typography variant="h5">Summary</Typography>
              <Typography>{intelligence.summary}</Typography>
            </Stack>
          </DashboardCard>

          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <DashboardCard>
                <SectionHeader eyebrow="Knowledge Agent" title="Top Findings" description="Structured findings synthesized from configured search and LLM providers." />
                <Stack component="ul" spacing={1.5} sx={{ pl: 2 }}>
                  {intelligence.top_findings.map((finding) => (
                    <Typography key={finding} component="li">
                      {finding}
                    </Typography>
                  ))}
                </Stack>
              </DashboardCard>
            </Grid>
            <Grid item xs={12} md={6}>
              <DashboardCard>
                <SectionHeader eyebrow="Planner Output" title="Recommended Actions" description="Immediate actions for the selected goal and time window." />
                <Stack component="ul" spacing={1.5} sx={{ pl: 2 }}>
                  {intelligence.recommended_actions.map((action) => (
                    <Typography key={action} component="li">
                      {action}
                    </Typography>
                  ))}
                </Stack>
              </DashboardCard>
            </Grid>
          </Grid>

          <DashboardCard>
            <SectionHeader eyebrow="Sources" title="Provider Results" description="Search provider outputs used by the agent workflow." />
            <Stack spacing={1.5}>
              {intelligence.sources.map((source) => (
                <Box key={source.url} sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 2, p: 2 }}>
                  <Stack direction="row" spacing={1} alignItems="center">
                    <SourceIcon color="secondary" fontSize="small" />
                    <Typography fontWeight={800}>{source.title}</Typography>
                    <Chip label={source.provider} size="small" variant="outlined" />
                  </Stack>
                  <Typography component="a" href={source.url} target="_blank" rel="noreferrer" color="secondary" sx={{ display: 'inline-block', mt: 1 }}>
                    {source.url}
                  </Typography>
                </Box>
              ))}
            </Stack>
          </DashboardCard>
        </Stack>
      ) : null}
    </Stack>
  );
}

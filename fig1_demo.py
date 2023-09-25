import numpy as np
import matplotlib.pyplot as plt
import constants
import plot_helpers as ph
import plotting_functions as pf

np.random.seed(420)  # Set the random seed to a specific value for reproducibility

class fig1_demo:
    def __init__(self):

        self.unicorn_data = np.random.randint(0, 10, size=50)
        self.rainbow_data = np.random.randint(20, 30, size=50)

        self.ice_cream_flavors = ['Van.', 'Choc.', 'Straw.']
        self.penguin_data = np.random.randint(0, 50, size=len(self.ice_cream_flavors))

        self.horn_length_data = np.random.uniform(0, 10, size=100)
        self.magic_power_data = (3+0.2*self.horn_length_data)+np.random.randn(len(self.horn_length_data))

        self.months = ['January', 'February', 'March']
        self.wombat_species = ['Common', 'Hairy', 'Northern']
        self.happiness_data = np.random.randint(-10, 10, size=(len(self.months), len(self.wombat_species)))

        self.widgets = np.random.randint(0, 100, size=100)

        self.laughs_per_minute = np.random.gamma(5, scale=2, size=1000)

    def lineplot_unicorns_vs_rainbows(self, ax):
        x = np.arange(len(self.unicorn_data))
        ax.plot(x, self.unicorn_data, label='Unicorns')
        ax.plot(x, self.rainbow_data, label='Rainbows')
        ax.set_xlabel('Time')
        ax.set_ylabel('Count')
        ax.set_title('Unicorns vs. Rainbows')
        ax.legend(loc='center left', bbox_to_anchor=(0, 1.5))

    def barplot_ice_cream_flavors(self, ax):
        colors = plt.cm.tab20(np.arange(len(self.ice_cream_flavors)))
        ax.bar(self.ice_cream_flavors, self.penguin_data, color=colors)
        ax.set_xlabel('Ice Cream Flavors')
        ax.set_ylabel('Penguin ct.')
        ax.set_title('Flavors Consumed by Penguins')

    def scatterplot_horn_length_vs_magic_power(self, ax):
        ax.scatter(self.horn_length_data, self.magic_power_data, c='hotpink')
        ax.set_xlabel("Unicorn's Horn Length (cm)")
        ax.set_ylabel('Magic Power')
        ax.set_title("Horn Length vs. Magic Power")

    def annotated_heatmap_wombat_happiness(self, ax):
        ax, cbar = pf.create_annotated_posneg_heatmap(ax, self.happiness_data)
        ax.set_xticks(np.arange(len(self.wombat_species)))
        ax.set_yticks(np.arange(len(self.months)))
        ax.set_xticklabels(self.wombat_species)
        ax.set_yticklabels(self.months)
        ax.set_xlabel('Wombat Species')
        ax.set_ylabel('Months')
        ax.set_title('Wombat Happiness')
        cbar.set_label('Happiness')
        return ax

    def lineplot_widgets(self, ax):
        ax.plot(self.widgets)
        ax.set_xlabel('Time')
        ax.set_ylabel('Number of Widgets')
        ax.set_title('Widgets over Time')

    def histogram_laughs(self, ax):
        # Plot the histogram on the specified axis
        ax.hist(self.laughs_per_minute, bins=30, color='orange', edgecolor='black')
        # Set labels and title
        ax.set_xlabel('Laughs per Minute')
        ax.set_ylabel('Frequency')
        ax.set_title('Laughs per Minute')

    def plot_dashboard(self):
        """
        Plots the whole figure.
        """

        # This code defines a 2D list called mosaic that represents
        # the layout of the subplots in the figure.
        # Each element in the list corresponds to a subplot position.
        # Note that F takes up two rows and one column, and G takes up one row and two columns.
        mosaic = [['A','B','C'],
                  ['D', 'E','F'],
                  ['G', 'G', 'F']]

        # Create the figure and axes objects using the subplot_mosaic function
        fig, ax_dict = plt.subplot_mosaic(mosaic,  # Specify the layout of subplots using the mosaic parameter
                                          figsize=(constants.FIG_WIDTH, 5),  # Set the size of the figure in inches
                                          dpi=300,  # Set the resolution of the figure in dots per inch
                                          constrained_layout=True,  # Enable constrained layout for automatic adjustment
                                          gridspec_kw={'height_ratios': [1, 1, 1.5],
                                                       # Set the relative heights of the rows
                                                       'width_ratios': [1.5, 1.5,
                                                                        1]})  # Set the relative widths of the columns
        self.lineplot_unicorns_vs_rainbows(ax_dict['A'])
        self.barplot_ice_cream_flavors(ax_dict['B'])
        ph.make_blank_panel(ax_dict['C']) #Panel C is blank, we can fill in it by hand later
        self.scatterplot_horn_length_vs_magic_power(ax_dict['D'])
        self.annotated_heatmap_wombat_happiness(ax_dict['E'])
        self.histogram_laughs(ax_dict['F'])
        self.lineplot_widgets(ax_dict['G'])
        ph.label_panels_mosaic(fig, ax_dict, size = 14)
        return fig, ax_dict

fig1 = fig1_demo() #create the figure object
fig, axes = fig1.plot_dashboard() #create the figure
ph.save_figure(fig, 1) #and save it

